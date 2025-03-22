const mongoose = require('mongoose');
const fraudSchema = new mongoose.Schema({
  transactionId: String,
  riskScore: Number,
  flagged: Boolean
});
module.exports = mongoose.model('Fraud', fraudSchema);
