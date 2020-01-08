package com.yulanbo.bishe.model;

public class Courses {
    private Integer id;

    private String coursename;

    private String teachername;

    private Integer teacherid;

    private Integer stunumber;

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

    public String getTeachername() {
        return teachername;
    }

    public void setTeachername(String teachername) {
        this.teachername = teachername == null ? null : teachername.trim();
    }

    public Integer getTeacherid() {
        return teacherid;
    }

    public void setTeacherid(Integer teacherid) {
        this.teacherid = teacherid;
    }

    public Integer getStunumber() {
        return stunumber;
    }

    public void setStunumber(Integer stunumber) {
        this.stunumber = stunumber;
    }
}