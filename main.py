###############################################################
#--Learn Git Branching inner methods
#export tree
#import tree
#build level 
#import level
#show commands
#undo/reset

## Learn Git Branching

#--resolving deltas


#--------------------------90% usage------------------------------#


#_________________________git merge___________________________#
#-- merge creates a parent commit
# *main -> git merge bugFix
# *bugFix -> git merge main

#_________________________git rebase___________________________#
#-- rebase enables to have a linear sequence of commits
# *bugFix -> git rebase main
# *main -> git rebase bugFix #-update main such as it contains bugFix

#_________________________move in tree___________________________#
#--Head is the current branch on which one is situated -> the branch is linked to a commit so as the Head
#--git checkout commit # Detach head from branch to a specific commit
# git checkout HEAD^, git checkout main^^
# git checkout main~3, git checkout HEAD~4
# git branch -f main HEAD~3 #reassign a branch to a specific commit

#_________________________cancel changes___________________________#
# git reset --soft HEAD~1, git reset --hard HEAD~1 #undo last commit #works only in local
# git revert HEAD, git revert HEAD~1 # undo changes in remote -> make a new pushable commit that undo changes 



#-----------------------Remaining 10%------------------------------#
#________________________moving work around___________________________#
#--git cherry-pick <Commit1> <Commit2> <...>

#*main -> git cherry-pick C2 C4 (commits of branch feature)
#*main-> git rebase -i HEAD~4 (do a git branch -f main debug-commit first)

#--if there are bugs -> one may make a debug branch and debugging commits
#-- bugs has been resolved but don't wan't to merge all bugs commits (what to do?)

#--amend  historical commit:
#git rebase -i
#git commit --amend
#git rebase -i
#move main to the new head of tree
#better to use cherry-pick

#--Add milestone:
#git tag v1 c1
#git checkout v1


#coming back from holydays
#--git describe <ref> : diff between most recent commit and most recent tag
#<tag>_<numCommits>_g<hash>

#chains
#git checkout HEAD~^2~2


#________________________Contribute to other projects___________________________#
#https://kbroman.org/github_tutorial/pages/fork.html


