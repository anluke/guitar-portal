function sendMail(contactForm) {
    emailjs.send('gmail', 'guitar', {
            from_name: "Guitar Portal",
            to_email: "contactForm.emailaddress.value"
        }, 'N6_BpHp-n6GFioyxa')
        .then(
            function (response) {
                console.log('SUCCESS', reponse);
            },
            function (error) {
                console.log('FAILED', error);
            }
        );
    return false;
}

// console.log('hello');