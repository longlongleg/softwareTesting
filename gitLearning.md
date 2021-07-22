# Git使用步骤 #
1. **安装GIT**：链接：https://git-scm.com/downloads

2. **设置用户名邮箱**
	1. $ git config --global user.name "Your Name"
	2. $ git config --global user.email "email@example.com"
	
3. **设置本地Git库**：进入到电脑某个文件夹目录，使用git init命令变成git可以关联的库
4. **提交文件**
	1. git add test.txt
	2. git commit -m "add test.txt file"
	
5.  **将本地库与远程的Github库相关联**
	1.  查看自己电脑C盘用户目录下面是否有.ssh文件夹
	2.  如果有则进行步骤6，没有进行下面步骤
	3.  在git bash运行命令创建.ssh目录：ssh-keygen -t rsa -C "youremail@example.com"
	4.  可以看到.ssh文件夹下面有id_rsa和id_rsa.pub两个文件
6.   **配置github SSH Key**
	1.   登录github，点击settings，找到SSH and GPG keys添加SSH key，title随意，key填入id_rsa.pub的内容进行保存即可
	  
7.   **新建库 new Repository**:在github上面新建库，如softwareTesting

8.   **关联库**：git remote add origin git@github.com:longlongleg/softwareTesting.git

9.   **本地库上传到远程库**:git push -u origin master

10.   **远程库下载到本地库**
	1.   第一次全部下载下来：git clone git@github.com:longlongleg/softwareTesting.git
	2.   后面只下载更新的内容：git pull origin master
	
11.   **其他详细命令**：网上百度：https://www.liaoxuefeng.com/wiki/896043488029600

	
