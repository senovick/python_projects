from docxtpl import DocxTemplate

doc = DocxTemplate("cover_letter_example.docx")
context = {'company': "Global Enterprise",
           'hiring_manager': 'Tony Stark',
           'company_address': '123 Enterprise Drive Somewhere, NA 12345',
           'date': '12/14/2022',
           'current_company': 'My Company',
           'years_service': '20',
           'name': 'Sean Novick',
           'email': 'sean.novick@gmail.com',
           'phone': '867-5309'}
doc.render(context)
doc.save("cover_letter.docx")