from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        
    def header(self):
        # Set the header for the PDF
        self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(60, 1, 'Log Report', 0, 0, 'R')
        self.ln(20)
        
    def footer(self):
        # Set the footer for the PDF
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def print_page(self, image):
        # Add a new page and print an image on it
        self.add_page()
        self.image(image, 15, 25, self.WIDTH - 30)