
#imporing selenium module for using chrome
from selenium import webdriver
#importing time module
from time import sleep
#importing keys to scroll end of a page sending keys
from selenium.webdriver.common.keys import Keys


# creating intsabot class as user name and password class attributes
# placing time delay in between for time taken to load pages

#creating class logs in on insta and opens the profile page
class Instabot:
    def __init__(self,user_name,pwd):
        self.user_name=user_name
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(5)

        user_name_link=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        user_name_link.send_keys((user_name))
        pw_=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")
        pw_.send_keys(pwd)
        login=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
        login.click()
        sleep(5)
        profile_site=self.driver.get("https://www.instagram.com"+"/"+user_name+"/")
        sleep(5)

        #deifinition to get followeing list from profile

    def get_following(self):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()


        sleep(5)
        a=['v']
        b=['z']
        #condition to scroll and check and input all followeing in the list
        while a!=b:
            b=a
            sleep(5)
            scroll=self.driver.find_element_by_xpath("//a[contains(@class,'notranslate')]")
            scroll.send_keys(Keys.END)

            sleep(5)

            list_=self.driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div')
            a=[x.text for x in list_]

            sleep(5)

        names=self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li")
        name = [name.text for name in names]
        followers_list=[x.split()[0] for x in name]
        self.driver.get("https://www.instagram.com"+"/"+self.user_name+"/")
        sleep(5)
        return followers_list

        #deifinition to return followers list from profile

    def get_followers(self):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        sleep(5)
        a=['v']
        b=['z']

        #condition to scroll and check and input all followers in the list

        while a!=b:
            b=a
            sleep(5)

            scroll=self.driver.find_element_by_xpath("//a[contains(@class,'notranslate')]")
            scroll.send_keys(Keys.END)
            sleep(5)



            list_=self.driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div')
            a=[x.text for x in list_]
            sleep(5)

        names=self.driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/ul/div/li")
        name = [name.text for name in names if name!='']
        following_list=[x.split()[0] for x in name]
        self.driver.get("https://www.instagram.com"+"/"+ self.user_name +"/")
        sleep(5)
        return following_list

        #deifinition to check followers and following list
        #calls following and followers deifinition , place them it two list and
        #checks the list with one another and returns list with names in following_list
        #but not in followers list

    def get_unfollowing (self):
        not_following=[]
        following=self.get_following()
        sleep(5)
        followers=self.get_followers()
        sleep(5)
        for i in following:
            m=0
            for j in followers:

                if i==j:

                    m=1
            if m==0:

                not_following.append(i)



        return (not_following)



j=Instabot('jt_zt','thapa11')
print(j.get_unfollowing())
