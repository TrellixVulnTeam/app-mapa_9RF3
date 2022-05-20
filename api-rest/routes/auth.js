const express = require('express'),
router = express.Router(),
{ _create, _finByUsername } = require('../controllers/users'),
passport = require('passport'),
jwt = require('jsonwebtoken');

router.post('/login', async(req, res, next) => {
    passport.authenticate('local', { session: false }, function(err, rutuser, info){
        if (err) return res.status(500).json(err);
        if (!rutuser) return res.status(400).json(info);
        const token = jwt.sign(rutuser, 'blabla', { expiresIn: '1h'});
        return res.status(200).json({
            token, expiresIn: 3600, rutuser
        });
    })(req, res, next);
});

router.post('/signup', async(req, res) =>{
    try{
        const foundUser = await _finByUsername(req.body.rutuser);
        if (foundUser) {
            return res.status(400).json('El rut ' + foundUser.rutuser + ' ya esta registrado')
        }

        const parking_user = await _create(req.body);
        return res.status(201).json({
            status: 'success',
            message: 'El usuario ' + parking_user.rutuser + ' fue creado satisfactoriamente...'
        })
    } catch (e) {
        return res.status(500).json(e.message);
    }
});

module.exports = router;