var res = confirm('Правило!!!!!');
if (res)
    console.log('Hello, JS');
else
    alert('Привет!');

document.writeln('Спасибо, что посетил мой сайт :D');

function innerHTMLMessage()
{
    var spanElement = document.getElementsByClassName('text'); // getElementById('...') - вернет тэг вроде
    var Text = 'Он работает коряво, но главное ведь, что работает! :)))';
    var newText =' ';
    newText = '<br>' + Text;

    spanElement[0].innerHTML = newText;
}

function getCurrentTime()
{
    var currentDate = new Date();
    var year = currentDate.getFullYear();
    var month = currentDate.getUTCMonth();
    var day = currentDate.getUTCDate(); //UTCDay какой-то не такой:) для дня
    var hours = currentDate.getUTCHours()+7; //значение по гринвическому меридиану, но с +7 вернет наше
    var minutes = currentDate.getUTCMinutes();
    var seconds = currentDate.getUTCSeconds();

    if (month<=9)
    {
        month = '0' + month;
    }
    if (day<=9)
    {
        day+='0'
    }
    if (hours<=9)
    {
        hours+='0'
    }
    if (minutes<=9)
    {
        minutes+='0'
    }
    if (seconds<=9)
    {
        seconds+='0'
    }

    var today = year + '-' + month + '-' + day;
    today+='T';
    today+= hours + ':' + minutes + ':' + seconds;

    console.log(today);
    return today;
}

function  Timer()
{
    var today = getCurrentTime();
    var counter = document.getElementsByClassName('timer')
    counter[0].innerHTML = today;
}
var i = 0;
function change(selector)
{
    var element = document.querySelector(selector);
    var color = ['pink', 'red', 'blue', 'green', 'blue', 'red', 'pink'];
    element.style.backgroundColor = color[i];
    i = (i + 1)%color.length;
}