{% extends "layout.html" %}
{% block title %}Update Pay Rate{% endblock %}
{% block page %}Update Pay Rate{% endblock %}
{{ super() }}


{% block content %}
<style>
    ::placeholder {
      color: rgba(0, 0, 0, 0.849);
    }
  
  </style>

<div>
    <div>
        <form id="updatePayForm" method="POST" action="/updatepay/{{rate.id}}" style= "border-radius: 25px; border: 2px solid #000000; padding: 155px;  padding-top: 50px; padding-bottom: 50px;">
    
            <label for="staffType">Choose the semester it is offered:</label>
            <select name="staffType">
                <option value="Lecturer" {% if rate.staff_type == 'Lecturer' %} selected {% endif %}>Lecturer</option>
                <option value="Instructor" {% if rate.staff_type == 'Instructor' %} selected {% endif %}>Instructor</option>
                <option value="Teaching Assistant" {% if rate.staff_type == 'Teaching Assistant' %} selected {% endif %}>Teaching Assistant</option>
                <option value="Tutor" {% if rate.staff_type == 'Tutor' %} selected {% endif %}>Tutor</option>      
            </select>
            
            <label for="status">Choose the semester it is offered:</label>
            <select name="status">
                <option value="Full Time" {% if rate.status == 'Full Time' %} selected {% endif %}>Full Time</option>
                <option value="Part Time" {% if rate.status == 'Part Time' %} selected {% endif %}>Part Time</option>      
            </select>

            <div class="row">
                <div class="input-field col s12">
                    <p>Pay Rate</p>
                    <input placeholder="{{rate.pay}}"  value="{{rate.pay}}" name="payRate" id="payRate" type="text" class="validate" style="color:#000000; border-radius: 35px; height: 25px; border: 2px solid #6d6d6d62; padding: 9px;">
                </div>
            </div>
            <div class="row justify-content-start">
                <div class="col s4 card-action">
                  <input type="submit" class="btn btn-secondary" value="Update Pay Rate" style="border-radius: 12px;">
                </div>
            </div> 
        </form>
    </div>
</div>

{% endblock %}
