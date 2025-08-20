export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  // Getter and Setter for code
  get code() {
    return this._code;
  }

  set code(newCode) {
    this._code = newCode;
  }

  // Getter and Setter for name
  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = newName;
  }

  // Method
  displayFullCurrency() {
    return `${this.name} ${(this.code)}`;
  }
}
