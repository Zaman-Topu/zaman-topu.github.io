// আজকের তারিখ থেকে ১০ দিন পরের একটি সময় সেট করা হলো
const launchDate = new Date();
launchDate.setDate(launchDate.getDate() + 10); // বর্তমান তারিখ + ১০ দিন

const countdown = () => {
    const now = new Date().getTime();
    const gap = launchDate - now;

    // সময় হিসাব (মিলিসেকেন্ড থেকে)
    const second = 1000;
    const minute = second * 60;
    const hour = minute * 60;
    const day = hour * 24;

    // সংখ্যা বের করা
    const textDay = Math.floor(gap / day);
    const textHour = Math.floor((gap % day) / hour);
    const textMinute = Math.floor((gap % hour) / minute);
    const textSecond = Math.floor((gap % minute) / second);

    // HTML এ আপডেট করা
    document.getElementById("days").innerText = textDay < 10 ? '0' + textDay : textDay;
    document.getElementById("hours").innerText = textHour < 10 ? '0' + textHour : textHour;
    document.getElementById("minutes").innerText = textMinute < 10 ? '0' + textMinute : textMinute;
    document.getElementById("seconds").innerText = textSecond < 10 ? '0' + textSecond : textSecond;

    // যদি সময় শেষ হয়ে যায়
    if (gap < 0) {
        document.querySelector('.countdown').innerHTML = "<h2>We Have Launched!</h2>";
    }
};

// প্রতি ১ সেকেন্ড পর পর আপডেট হবে
setInterval(countdown, 1000);