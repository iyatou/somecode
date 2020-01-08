package com.yulanbo.bishe.receiveInfo;

public class BindInfo {
    private String useremail;
    private String username;
    private String birthday;
    private String school;
    private String sex;
    private String identify;

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getUseremail() {
        return useremail;
    }

    public void setUseremail(String useremail) {
        this.useremail = useremail;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }

    public String getIdentify() {
        return identify;
    }

    public void setIdentify(String identify) {
        this.identify = identify;
    }

    @Override
    public String toString() {
        return "BindInfo{" +
                "useremail='" + useremail + '\'' +
                ", username='" + username + '\'' +
                ", birthday='" + birthday + '\'' +
                ", school='" + school + '\'' +
                ", sex='" + sex + '\'' +
                ", identify='" + identify + '\'' +
                '}';
    }
}
