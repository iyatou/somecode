package com.yulanbo.bishe.model;

public class Questions {
    private Integer id;

    private String type;

    private String lessionname;

    private String questionname;

    private String choice;

    private String rightkey;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type == null ? null : type.trim();
    }

    public String getLessionname() {
        return lessionname;
    }

    public void setLessionname(String lessionname) {
        this.lessionname = lessionname == null ? null : lessionname.trim();
    }

    public String getQuestionname() {
        return questionname;
    }

    public void setQuestionname(String questionname) {
        this.questionname = questionname == null ? null : questionname.trim();
    }

    public String getChoice() {
        return choice;
    }

    public void setChoice(String choice) {
        this.choice = choice == null ? null : choice.trim();
    }

    public String getRightkey() {
        return rightkey;
    }

    public void setRightkey(String rightkey) {
        this.rightkey = rightkey == null ? null : rightkey.trim();
    }
}