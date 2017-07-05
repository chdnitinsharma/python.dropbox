#from dropbox import DropboxOAuth2FlowNoRedirect
import dropbox

APP_KEY=""
APP_SECRET=""
auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

authorize_url = auth_flow.start()
print "1. Go to: " + authorize_url
print "2. Click \"Allow\" (you might have to log in first)."
print "3. Copy the authorization code."
auth_code = raw_input("Enter the authorization code here: ").strip()


try:
    oauth_result = auth_flow.finish(auth_code)
except Exception, e:
    print('Error: %s' % (e,))
    

dbx = dropbox.Dropbox(oauth_result.access_token)

accountInfo=dbx.users_get_current_account()

"""
file_upload_=open("./demo.png","r")
dbx.files_upload(file_upload_.read(), '/demo.png');
file_upload_.close();
"""

print "-"*40

print "Account Id: ",accountInfo.account_id;
print "Display Name: ",accountInfo.name.display_name;
print "Given Name: ",accountInfo.name.given_name;
print "Email: ",accountInfo.email;
print "Referral Link: ",accountInfo.referral_link;
print "Account Type: ",accountInfo.account_type;
print "Profile Photo Url Type: ",accountInfo.profile_photo_url;
print "Country Photo Url Type: ",accountInfo.country;

print "-"*40
#upload Text file
#dbx.files_upload("Demo text file ", '/Resume/Python/demo.txt')

print "-"*40

for entry in dbx.files_list_folder('',recursive=True).entries:
	print( entry.path_display+"============"+entry.name)
    
print "-"*40

