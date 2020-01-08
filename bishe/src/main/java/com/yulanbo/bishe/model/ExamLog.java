package com.yulanbo.bishe.model;

import java.util.Date;

public class ExamLog {
    private Integer id;

    private Integer uploaderid;

    private String uploadername;

    private Date starttime;

    private Date endtime;

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

    public Date getStarttime() {
        return starttime;
    }

    public void setStarttime(Date starttime) {
        this.starttime = starttime;
    }

    public Date getEndtime() {
        return endtime;
    }

    public void setEndtime(Date endtime) {
        this.endtime = endtime;
    }
}