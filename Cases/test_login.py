from Pages.LoginPage import Login

p = Login()
p.gotos()
p.inputUser('admin')
p.inputPassword('admin123')
result=p.login()
assert result=='yes'