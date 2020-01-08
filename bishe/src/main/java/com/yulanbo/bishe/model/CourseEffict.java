package com.yulanbo.bishe.model;

public class CourseEffict {
    private Integer id;

    private Integer courseid;

    private String coursename;

    private String lessionrate;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getCourseid() {
        return courseid;
    }

    public void setCourseid(Integer courseid) {
        this.courseid = courseid;
    }

    public String getCoursename() {
        return coursename;
    }

    public void setCoursename(String coursename) {
        this.coursename = coursename == null ? null : coursename.trim();
    }

    public String getLessionrate() {
        return lessionrate;
    }

    public void setLessionrate(String lessionrate) {
        this.lessionrate = lessionrate == null ? null : lessionrate.trim();
    }
}