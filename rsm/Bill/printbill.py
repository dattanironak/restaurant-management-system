import io, sys
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from .models import Bill, BillMenu



def print_bill(bid):
    # Create a file-like buffer to receive PDF data.
    print("In print bill")
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    bill = Bill.objects.get(id=bid)
    bill_pdf = str(bill.id) + ".pdf"
    p = canvas.Canvas(bill_pdf)
    p.translate(0, 840)

    p.drawImage('D:\Study\Sem-4\SP\Project\Restaurant management System\\restaurant-management-system\\rsm\Bill\logo_swad.png', 50,-90, 180, 80)
    p.drawString(50, -100, "Swad Restaurant")
    p.drawString(50, -125, "GST No : ABCDEFGHIJK")
    p.drawString(50, -150, "Table No : " + str(bill.table_no))
    p.drawString(50, -175, "Time : " + str(bill.bill_date))


    items = BillMenu.objects.filter(bill_id=bid)
    i = 0
    total = 0
    data = [["No.", "Item Name", "Quantity", "Price", "Total"]]
    for item in items:
        data.append([i + 1, item.item_name, item.quantity, item.item_price, item.item_total])
        total = total + item.item_total
        i=i+1

    j=i
    while(i<30):
        data.append([])
        i=i+1
    data.append([None,None, None, "TOTAL : ", total])

    t = Table(data, style = [('GRID', (0,0), (-1,j), 1, colors.black),
                             ("BOX", (0,0), (-1,-1), 2, colors.black),
                             ("LINEBEFORE", (0, 0), (1, -1), 1, colors.black),
                             ("LINEBEFORE", (2, 0), (2, -1), 1, colors.black),
                             ("LINEBEFORE", (3, 0), (3, -1), 1, colors.black),
                             ("LINEBEFORE", (4, 0), (4, -1), 1, colors.black)
                             ])




    t.wrapOn(p, 650, 550) #Table Width nd height
    t.drawOn(p, 50, -800)
    p.drawString(50, -820, "Thank you for visiting !")

    # Draw things on the PDF. Here's where the PDF generation happens.


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    bill.is_printed = True
    bill.save()
    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return bill_pdf
