function sendMail(contactForm) {
    emailjs.send('gmail', 'guitar', {
            'to_email': contactForm.email.value,
        })
        .then(
            function (response) {
                console.log('SUCCESS', response);
            },
            function (error) {
                console.log('FAILED', error);
            }
        );
}