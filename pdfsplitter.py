from PyPDF2 import PdfFileReader, PdfFileWriter


def splitter(filename):
    inputPdf = PdfFileReader(open(filename, "rb"))

    for page in range(inputPdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(inputPdf.getPage(page))

        output_filename = '{}_page_{}.pdf'.format(
            filename, page+1)

    with open(output_filename, 'wb') as out:
         pdf_writer.write(out)

         print('Created: {}'.format(output_filename))
