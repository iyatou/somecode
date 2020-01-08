package com.yulanbo.bishe.model;

import java.util.Date;

public class LessionTest {
    private Integer id;

    private String lessionname;

    private Integer questionid;

    private String rightrate;

    private Date changetime;

    private Integer courseid;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLessionname() {
        return lessionname;
    }

    public void setLessionname(String lessionname) {
        this.lessionname = lessionname == null ? null : lessionname.trim();
    }

    public Integer getQuestionid() {
        return questionid;
    }

    public void setQuestionid(Integer questionid) {
        this.questionid = questionid;
    }

    public String getRightrate() {
        return rightrate;
    }

    public void setRightrate(String rightrate) {
        this.rightrate = rightrate == null ? null : rightrate.trim();
    }

    public Date getChangetime() {
        return changetime;
    }

    public void setChangetime(Date changetime) {
        this.changetime = changetime;
    }

    public Integer getCourseid() {
        return courseid;
    }

    public void setCourseid(Integer courseid) {
        this.courseid = courseid;
    }
}