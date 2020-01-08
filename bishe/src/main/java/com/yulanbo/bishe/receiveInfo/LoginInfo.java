package com.yulanbo.bishe.receiveInfo;

public class LoginInfo {
    private String useremail;
    private String password;

    public String getUseremail() {
        return useremail;
    }

    public void setUseremail(String useremail) {
        this.useremail = useremail;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @Override
    public String toString() {
        return "LoginInfo{" +
                "useremail='" + useremail + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
