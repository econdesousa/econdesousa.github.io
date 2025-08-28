import scholarly
import markdown_it
from scholarly import scholarly



def get_publications(scholar_id):
    """
    Fetches and returns a list of publications from Google Scholar.
    """
    try:
        # Search for the author by ID and get the first result
        search_query = scholarly.search_author(scholar_id)
        author = next(search_query)
        
        # Fill the author's profile with their publications
        author = scholarly.fill(author, sections=['publications'])
        
        publications = [pub for pub in author.publications]
        print(f"Found {len(publications)} publications.")
        return publications
    except Exception as e:
        print(f"Error fetching data from Google Scholar: {e}")
        return []

# ... the rest of your script

def format_publications_markdown(publications):
    """
    Formats the list of publications into Markdown.
    """
    md_content = "# Publications list\n\n"
    md_content += "### Publications in peer reviewed journals\n\n"

    # Sort publications by year in descending order
    publications.sort(key=lambda x: x.bib.get('year', 0), reverse=True)

    for i, pub in enumerate(publications, 1):
        bib = pub.bib
        title = bib.get('title', 'N/A')
        authors = bib.get('author', 'N/A')
        journal = bib.get('journal', bib.get('booktitle', 'N/A'))
        year = bib.get('year', 'N/A')
        
        md_content += f"{i}. **{authors}**, {title}, *{journal}*, {year}\n\n"
    
    return md_content

if __name__ == "__main__":
    # Replace with your Google Scholar ID
    SCHOLAR_ID = 'xi0xi2AAAAAJ'
    
    try:
        # Read the existing content of the Publications.md file
        with open("Publications.md", "r") as f:
            original_content = f.read()

        # Generate the new publications section
        publications = get_publications(SCHOLAR_ID)
        new_publications_section = format_publications_markdown(publications)
        
        # Replace the old publications section with the new one
        # This assumes original file has a section header that we can find
        # and replace. This is a simple but effective method.
        # It will only replace the text between "# Publications list" and "### Publications in conference proceedings".
        start_marker = "# Publications list\n\n"
        end_marker = "### Publications in conference proceedings"
        
        if start_marker in original_content and end_marker in original_content:
            # Get the content before and after the publications section
            pre_content = original_content.split(start_marker)[0] + start_marker
            post_content = original_content.split(end_marker)[1]
            
            # Combine everything back together
            updated_content = pre_content + new_publications_section + "\n" + end_marker + post_content
        else:
            # If the markers are not found, fallback to just writing the new content
            updated_content = new_publications_section

        # Write the updated content back to the Publications.md file
        with open("Publications.md", "w") as f:
            f.write(updated_content)
            
        print("Publications page updated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")