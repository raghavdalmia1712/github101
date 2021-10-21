setInterval(() => {
    d=new Date();
    m=d.getMinutes();
    h=d.getHours();
    s=d.getSeconds();
    hrota=30*h+m/2;
    mrota=6*m;
    srota=6*s;
    
    hour.style.transform=`rotate(${hrota}deg)`;
    minute.style.transform=`rotate(${mrota}deg)`;
    second.style.transform=`rotate(${srota}deg)` ;

}, 1000);