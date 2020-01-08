package com.yulanbo.bishe.model;

public class StuLessionRate {
    private Integer id;

    private Integer stuid;

    private String stuname;

    private Integer barnum;

    private String nowaddress;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getStuid() {
        return stuid;
    }

    public void setStuid(Integer stuid) {
        this.stuid = stuid;
    }

    public String getStuname() {
        return stuname;
    }

    public void setStuname(String stuname) {
        this.stuname = stuname == null ? null : stuname.trim();
    }

    public Integer getBarnum() {
        return barnum;
    }

    public void setBarnum(Integer barnum) {
        this.barnum = barnum;
    }

    public String getNowaddress() {
        return nowaddress;
    }

    public void setNowaddress(String nowaddress) {
        this.nowaddress = nowaddress == null ? null : nowaddress.trim();
    }
}