
///////////////////////
// PYTHON LIB FOR SHAREPOINT LIST
//////////////////////
!pip install Office365-REST-Python-Client

///////////////////////
// READ ALL ITEMS IN SHAREPOINT LIST
//////////////////////
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
site_url = "https://fengbuedu.sharepoint.com/sites/Otor"
sp_list = "ORDER"
ctx = ClientContext(site_url).with_credentials(UserCredential("mahmoud.taha17@feng.bu.edu.eg", "Omabdo2020"))
sp_lists = ctx.web.lists
s_list = sp_lists.get_by_title(sp_list)
l_items = s_list.get_items()
ctx.load(l_items)
ctx.execute_query()

for item in l_items:
    print(item.properties['SHEIKH_NAME'],item.properties['COST'])


///////////////////////
// UPDATE ITEMS IN SHAREPOINT LIST
//////////////////////
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
site_url = "https://fengbuedu.sharepoint.com/sites/Otor"
sp_list = "ORDER"
ctx = ClientContext(site_url).with_credentials(UserCredential("mahmoud.taha17@feng.bu.edu.eg", "Omabdo2020"))
sp_lists = ctx.web.lists
s_list = sp_lists.get_by_title(sp_list)
l_items = s_list.get_items()

item = s_list.get_item_by_id(496)
item.set_property('SHEIKH_NAME', 'HAMADA')
item.set_property('COST', '999')
item.update()
ctx.execute_query()