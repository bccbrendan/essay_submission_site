<!-- submission template form
     bottle template variables:
         essay_title - e.g. 'Literary Essay'
         char_len    - max essay length
         site_url    - the root url for this website
-->
<HTML>
<HEAD>
<script language = "Javascript">

function taLimit()
{
    var taObj=event.srcElement;
    if (taObj.value.length==taObj.maxLength*1) return false;
}

function taCount(visCnt)
{
    var taObj=event.srcElement;
    if (taObj.value.length>taObj.maxLength*1) taObj.value=taObj.value.substring(0,taObj.maxLength*1);
    if (visCnt) visCnt.innerText=taObj.maxLength-taObj.value.length;
}
</script>
</HEAD>

<BODY>
<a href="/literary_essay">Literary Essay</a>&nbsp&nbsp
<a href="/expository_essay">Expository Essay</a>&nbsp&nbsp
<a href="/persuasive_essay">Persuasive Essay</a>&nbsp&nbsp
<a href="/single_selection_oer">Single Selection OER</a>&nbsp&nbsp
<a href="/crossover_oer">Crossover OER</a>&nbsp&nbsp
<br><br>
<b>{{essay_title}}</b><br>
<font>
<table><tr><td>
<FORM action="{{site_url}}/essay_submission" method="post">
    <p>
    First name: <INPUT type="text" name="firstname"><BR>
    Last name: <INPUT type="text" name="lastname"><BR>
    Period: <select name="period">
        <option value="1st">1st</option>
        <option value="2nd">2nd</option>
        <option value="3rd">3rd</option>
        <option value="4th">4th</option>
        <option value="6th">6th</option>
        <option value="7th">7th</option>
        <option value="8th">8th</option>
    </select><br>

    <TEXTAREA onkeypress="return taLimit()" onkeyup="return taCount(myCounter)"
    name=essay rows=25 wrap=physical cols=70 maxLength="{{char_len}}" name="essay"
    spellcheck="false"></TEXTAREA><br>
    Characters left : <B><SPAN id=myCounter>{{char_len}}</SPAN></B>
    <INPUT type="hidden" name="essay_type" value="{{essay_title}}">
    <INPUT type="submit" value="Send"> <INPUT type="reset">
    </p>
</FORM>
</td><td valign="Top">
</table>
</font>
</BODY>
</HTML>
