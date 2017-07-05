import dropbox

GENERATED_ACCESS_TOKEN='';
dbx = dropbox.Dropbox(GENERATED_ACCESS_TOKEN)


accountInfo=dbx.users_get_current_account()

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

"""
#upload file on Dropbox
file_upload_=open("./demo.png","r")
dbx.files_upload(file_upload_.read(), '/demo.png');
file_upload_.close();
"""
"""
#Upload zip file
file_upload_zip=open("./demo.png.zip","r")
dbx.files_upload(file_upload_zip.read(), '/demo.png.zip');
file_upload_zip.close();
"""

#upload Text file
#dbx.files_upload("Demo text file ", '/Resume/Python/demo.txt')

print "-"*40

for entry in dbx.files_list_folder('',recursive=True).entries:
    print( entry.path_display+"============"+entry.name)
    
print "-"*40

