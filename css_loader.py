from pyscript import document, window

# Function to apply landscape styles
def apply_landscape_styles():
    # Replace this with your landscape styles
    document.body.classList.remove('phone')
    document.body.classList.add('desktop')

# Function to apply portrait styles
def apply_portrait_styles():
    # Replace this with your portrait styles
    document.body.classList.remove('desktop')
    document.body.classList.add('phone')

# Function to show the content
def show_content():
    # Select and show the content elements
    content_elements = document.querySelectorAll('.main-grid, .header, .sidebar, .main')
    for element in content_elements:
        element.style.display = 'block'

# Check screen dimensions
def check_screen_dimensions():
    if window.innerWidth > window.innerHeight:
        # Landscape orientation
        apply_landscape_styles()
    else:
        # Portrait orientation
        apply_portrait_styles()

# Wait for the DOM to fully load before running the code
document.addEventListener('DOMContentLoaded', check_screen_dimensions)

# Once the code has executed, show the content
window.addEventListener('load', show_content)
