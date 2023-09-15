from typing import List, Dict

def generate_body(papers: List[Dict[str,str]]):
    style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            color: #333;
        }
        .paper {
            border: 1px solid #e0e0e0;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .paper-title {
            font-size: 18px;
            margin-bottom: 10px;
        }
        .paper-title a {
            text-decoration: none;
            color: #007BFF;
        }
        .paper-title a:hover {
            text-decoration: underline;
        }
        .paper-authors {
            font-size: 16px;
            margin-bottom: 10px;
            color: #555;
        }
        .paper-abstract {
            font-style: italic;
        }
    </style>
    """

    # Paper templates
    body_content = ""
    for paper in papers:
        body_content += f"""
        <div class="paper">
            <div class="paper-title">
                <a href="{paper['main_page']}">{paper['title']}</a>
            </div>
            <div class="paper-authors">
                Authors: {paper['authors']}
            </div>
            <div class="paper-abstract">
                Abstract: {paper['abstract']}
            </div>
        </div>
        """

    return style + body_content