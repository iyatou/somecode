package com.yulanbo.bishe.receiveInfo;

public class RegisterInfo {
    private String useremail;
    private String password;
    private String repassword;
    private String code;

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

    public String getRepassword() {
        return repassword;
    }

    public void setRepassword(String repassword) {
        this.repassword = repassword;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    @Override
    public String toString() {
        return "RegisterInfo{" +
                "useremail='" + useremail + '\'' +
                ", password='" + password + '\'' +
                ", repassword='" + repassword + '\'' +
                ", code='" + code + '\'' +
                '}';
    }
}
