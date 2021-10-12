git remote add upstream git@git.intramundi.com:network/repo.git
#check if upstream has been added
git remote -v
#if the original repo has been 
git fetch upstream
git rebase upstream/master
git push -f origin master
#if the original repo has not been altered
git pull upstream master
git push origin master
#To bring only some branches from upstream repo :
git fetch upstream
git checkout <the original repo branch to transfer>
git push origin <the original repo branch to transfer>