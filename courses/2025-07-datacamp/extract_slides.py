# /// script
# dependencies = [
# ]
# ///

import os
import re
from pathlib import Path

def parse_outline_file(file_path):
    """Parse a single outline file and extract slides"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    slides = []
    
    # Find all slide sections
    slide_sections = re.findall(r'### Slides\n(.*?)(?=\n---|$|\n##)', content, re.DOTALL)
    
    # Extract chapter/lesson info from file path and content
    chapter_match = re.search(r'chapter-(\d+)', str(file_path))
    chapter_num = chapter_match.group(1) if chapter_match else "Unknown"
    
    # Find lesson titles in the content
    lesson_titles = re.findall(r'## Lesson \d+\.\d+: "([^"]+)"', content)
    if not lesson_titles:
        # Try alternative format
        lesson_titles = re.findall(r'# Chapter \d+: ([^\n]+)', content)
    
    for i, section in enumerate(slide_sections):
        lesson_title = lesson_titles[i] if i < len(lesson_titles) else "Overview"
        
        # Extract individual slides
        slide_items = re.findall(r'^\d+\.\s*(.+)$', section, re.MULTILINE)
        
        for j, slide_content in enumerate(slide_items, 1):
            slides.append({
                'chapter': f"Chapter {chapter_num}",
                'lesson': lesson_title,
                'slide_num': j,
                'content': slide_content.strip()
            })
    
    return slides

def generate_markdown_table(all_slides):
    """Generate markdown table from slides data"""
    
    if not all_slides:
        return "No slides found."
    
    # Create markdown table
    table = "# Course Slides Overview\n\n"
    table += "| Chapter | Lesson | Slide | Content |\n"
    table += "|---------|--------|-------|----------|\n"
    
    prev_chapter = None
    prev_lesson = None
    
    for slide in all_slides:
        # Add chapter break
        if prev_chapter and slide['chapter'] != prev_chapter:
            table += "| | | | |\n"  # Empty row
            table += "| **---** | **---** | **---** | **---** |\n"  # Separator row
            table += "| | | | |\n"  # Empty row
        
        # Add lesson break (but not after chapter break)
        elif prev_lesson and slide['lesson'] != prev_lesson and slide['chapter'] == prev_chapter:
            table += "| | | | |\n"  # Empty row between lessons
        
        # Escape pipe characters in content
        content = slide['content'].replace('|', '\\|')
        table += f"| {slide['chapter']} | {slide['lesson']} | {slide['slide_num']} | {content} |\n"
        
        prev_chapter = slide['chapter']
        prev_lesson = slide['lesson']
    
    return table

def main():
    """Main function to process all course files"""
    
    # Get the content directory
    content_dir = Path(__file__).parent / "content"
    
    if not content_dir.exists():
        print(f"Content directory not found: {content_dir}")
        return
    
    all_slides = []
    
    # Process each chapter directory
    for chapter_dir in sorted(content_dir.glob("chapter-*")):
        if chapter_dir.is_dir():
            # Look for outline files
            for outline_file in chapter_dir.glob("*outline*.md"):
                print(f"Processing: {outline_file}")
                try:
                    slides = parse_outline_file(outline_file)
                    all_slides.extend(slides)
                    print(f"  Found {len(slides)} slides")
                except Exception as e:
                    print(f"  Error processing {outline_file}: {e}")
    
    # Generate and save markdown table
    if all_slides:
        markdown_table = generate_markdown_table(all_slides)
        
        output_file = Path(__file__).parent / "slides_overview.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_table)
        
        print(f"\nGenerated slides overview: {output_file}")
        print(f"Total slides found: {len(all_slides)}")
        
        # Also print to console
        print("\n" + markdown_table)
    else:
        print("No slides found in any outline files.")

if __name__ == "__main__":
    main() 