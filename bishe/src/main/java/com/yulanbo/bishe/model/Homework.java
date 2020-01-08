package com.yulanbo.bishe.model;

import java.util.Date;

public class Homework {
    private Integer id;

    private Integer uploaderid;

    private String uploadername;

    private Integer questionnum;

    private String achieverate;

    private String averageright;

    private String discribe;

    private Date uploadtime;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getUploaderid() {
        return uploaderid;
    }

    public void setUploaderid(Integer uploaderid) {
        this.uploaderid = uploaderid;
    }

    public String getUploadername() {
        return uploadername;
    }

    public void setUploadername(String uploadername) {
        this.uploadername = uploadername == null ? null : uploadername.trim();
    }

    public Integer getQuestionnum() {
        return questionnum;
    }

    public void setQuestionnum(Integer questionnum) {
        this.questionnum = questionnum;
    }

    public String getAchieverate() {
        return achieverate;
    }

    public void setAchieverate(String achieverate) {
        this.achieverate = achieverate == null ? null : achieverate.trim();
    }

    public String getAverageright() {
        return averageright;
    }

    public void setAverageright(String averageright) {
        this.averageright = averageright == null ? null : averageright.trim();
    }

    public String getDiscribe() {
        return discribe;
    }

    public void setDiscribe(String discribe) {
        this.discribe = discribe == null ? null : discribe.trim();
    }

    public Date getUploadtime() {
        return uploadtime;
    }

    public void setUploadtime(Date uploadtime) {
        this.uploadtime = uploadtime;
    }
}