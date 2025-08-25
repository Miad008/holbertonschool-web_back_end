export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // لما يتحول للكائن إلى رقم
  valueOf() {
    return this._size;
  }

  // لما يتحول للكائن إلى نص
  toString() {
    return this._location;
  }
}
