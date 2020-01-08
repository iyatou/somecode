package com.yulanbo.bishe.model;

public class VidioAddress {
    private Integer id;

    private String coursename;

    private String lessionname;

    private String barname;

    private String baraddress;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getCoursename() {
        return coursename;
    }

    public void setCoursename(String coursename) {
        this.coursename = coursename == null ? null : coursename.trim();
    }

    public String getLessionname() {
        return lessionname;
    }

    public void setLessionname(String lessionname) {
        this.lessionname = lessionname == null ? null : lessionname.trim();
    }

    public String getBarname() {
        return barname;
    }

    public void setBarname(String barname) {
        this.barname = barname == null ? null : barname.trim();
    }

    public String getBaraddress() {
        return baraddress;
    }

    public void setBaraddress(String baraddress) {
        this.baraddress = baraddress == null ? null : baraddress.trim();
    }
}