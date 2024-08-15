# study
study git

git status #查看repo的状态
git diff #查看文件的不同
git reset --hard Head^ #回到上一个提交

git fetch origin
git reset --hard origin/master #同步远程库
git checkout -- file-name #撤销文件的修改

git checkout -b branch-name #创建和切换到branch-name branch
git merge branch-name #合并branch-name branch到当前branch
git switch -c  branch-name #创建和切换到branch-name branch

git switch branch-name
git checkout branch-name 切换到到branch-name branch

git branch #查看branch
git branch branch-name #创建branch-name branch
git branch -d branch-name #删掉branch-name branch
a
b
 git log --graph --pretty=oneline --abbrev-commit

git merge --no-ff -m "merge with no-ff" dev #禁用fast forword,生成一个新的提交
test
