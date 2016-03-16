function toggleShow(id, btnid, btn) {
    if (document.getElementById(id).style.display == 'none') {
        document.getElementById(id).style.display = 'inline';
        document.getElementById(btnid).style.display = 'none';
        var input = document.getElementById('tagTextInput');
        input.focus();
        input.select();
    } else {
        document.getElementById(id).style.display = 'none';
        document.getElementById(btnid).style.display = 'inline';
    }
}