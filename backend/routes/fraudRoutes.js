const express = require('express');
const router = express.Router();
const Fraud = require('../models/Fraud');

router.get('/', async (req, res) => {
  const frauds = await Fraud.find();
  res.json(frauds);
});

module.exports = router;