from PyPDF2 import PdfReader, PdfWriter

reader_pdf  = PdfReader("./recoupment.pdf")
watermarker_pdf = PdfReader("./watermark_sk.pdf")
writer = PdfWriter()
#
# for page in reader_pdf.pages:
#     #Merging the watermarker onto the page
#     page.merge_page(watermarker_pdf.pages[0])
#     writer.add_page(page)
#
# #writing the output to a new file. A new output.pdf file is created
# with open("./output.pdf", "wb") as output_fle:
#     writer.write(output_fle)
#
# print(f"Watermarked PDF saved!")

#let's try for just one page
reader_pdf.pages[0].merge_page(watermarker_pdf.pages[0])
writer.add_page(reader_pdf.pages[0])

with open("./one_page_watermark.pdf", "wb") as one_page_file:
    writer.write(one_page_file)


