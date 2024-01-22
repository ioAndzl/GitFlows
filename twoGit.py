"""
How to configure two github account on a machine :

#generate ssh private and public keys
ssh-keygen -t rsa -C “your-email-address”  #-t > type, -C > comment -> choose file_name
/c/Users/your_username/.ssh/file_name

#> by default, filename is id_rsa

#add pub-key on github, name it after machine with one of following methods
#register keys on pc 

    - @mac ssh-add ~/.ssh/file_name

    #> in gitbash
    - eval $(ssh-agent)
    - ssh-add ~/.ssh/file_name


-------------to
add config file in .ssh folder
add :


# Personal account
Host github.com-ioAndzl
    HostName github.com
    User git
    IdentityFile ~/.ssh/ioandzl

# Fandzl account
Host github.com-octoandzl
    HostName github.com
    User git
    IdentityFile ~/.ssh/idrsa



[user]
    name = Aadil YUNUSH
    email = andzlhub@gmail.com


-------------to

in .gitconfig file
add :

[user]
        email = aadil.yunush@gmail.com
        name = Aadil
[includeIf "gitdir:~/ioandzl/"]
        path=~/ioAndzl/.gitconfig_ioandzl
[includeIf "gitdir:~/Work/"]
        path=~/Work/.gitconfig_work
[includeIf "gitdir:~/octoandzl/"]
        path=~/octoandzl/.gitconfig_octoandzl

[color]
        diff = auto
        status = auto
        branch = auto
~

-------------to

in .gitconfig_ioandzl file
add
[user]
    email = aadil.yunush@gmail.com
    name = ioandzl

~

--------test config 

git init
git config -l 
git config user.name
git config user.email



git add .
git commit -m "First commit"
git remote add origin git@github.com-ioAndzl:ioAndzl/repo_name.git
git push origin master

or 
git clone git@github.com-ioAndzl:ioAndzl/repo.git
"""




# ssh-keygen -t rsa -C "john@doe.com" -> id_rsa_doe_company
# ~/.ssh/id_rsa_doe_company.pub -> add to github 
# eval $(ssh-agent)
# ssh-add ~/.ssh/id_rsa_doe_company
# create a config file in .ssh 
# add :
#Host github-doe-company
#  HostName github.com
#  User git
#  IdentityFile ~/.ssh/id_rsa_doe_company
# eval $(ssh-agent)
#> add lines in config files
#> register others keys
# ssh-add ~/.ssh/id_rsa_visian
# ssh-add ~/.ssh/id_rsa_ioAndzl
# git remote add origin git@github-doe-company:username/repo.git
# git remote set-url origin git@github-doe-company:username/repo.git