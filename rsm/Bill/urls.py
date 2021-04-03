from django.urls import path
from . import views
from Bill import statement
from Bill import printbill

urlpatterns = [
    path('', views.bills),
    path('newbill/<table_no>', views.newbill),
    path('updatebill/<table_no>', views.updatebill),
    path('updatebill/<table_no>/<update_id>', views.updatebill),
    path('updatebill/deleteitem/<bill_id>/<delete_id>', views.deleteitem),
    path('print/<bid>', views.printbill_views),
    path('finish/<bid>', views.finish),
    path('statement', statement.statement),
    #path('printbill/<bid>', printbill.printbill)
]
