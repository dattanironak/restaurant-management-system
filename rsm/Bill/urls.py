from django.urls import path
from . import views
from Bill import statement
<<<<<<< HEAD
from Bill import printbill
=======
>>>>>>> 673f329fd7fcf909a38534e4fb7b8022537e44f1

urlpatterns = [
    path('', views.bills),
    path('newbill/<table_no>', views.newbill),
    path('updatebill/<table_no>', views.updatebill),
    path('updatebill/<table_no>/<update_id>', views.updatebill),
    path('updatebill/deleteitem/<bill_id>/<delete_id>', views.deleteitem),
<<<<<<< HEAD
    path('print/<bid>', views.printbill_views),
    path('finish/<bid>', views.finish),
    path('statement', statement.statement),
    #path('printbill/<bid>', printbill.printbill)
=======
    path('print/<bid>', views.print),
    path('finish/<bid>', views.finish),
    path('statement', statement.statement)
>>>>>>> 673f329fd7fcf909a38534e4fb7b8022537e44f1
]
