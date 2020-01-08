package com.yulanbo.bishe.responseinfo;

public class LoginRes {
    private String data;

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    private String username;
    private String identify;

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getIdentify() {
        return identify;
    }

    public void setIdentify(String identify) {
        this.identify = identify;
    }

    @Override
    public String toString() {
        return "LoginRes{" +
                "data='" + data + '\'' +
                ", username='" + username + '\'' +
                ", identify='" + identify + '\'' +
                '}';
    }
}
