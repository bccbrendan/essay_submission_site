<!--template page. 
    variables: 
    entries: repeated <tr>
    site_url: root url of website
-->
<HTML> 
<HEAD> 
<title>Submissions</title>
</HEAD> 
<BODY> 
Submission review
<br><br> 

<table border="1">
<tr>
<!-- TODO <td>[checkbox]</td> -->
<td>Time</td>
<td>Last</td>
<td>First</td>
<td>Period</td>
<td>Title link</td>
<td>emailed</td>
</tr>
{{!entries}}
</table>

<FORM action="{{site_url}}/delete_submissions" method="post">
    <INPUT type="submit" value="Delete all submissions"> 
</FORM>

</BODY>
</HTML>
