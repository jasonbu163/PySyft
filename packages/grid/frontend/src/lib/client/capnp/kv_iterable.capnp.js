'use strict';

/**
 * This file has been automatically generated by the [capnpc-ts utility](https://github.com/jdiaz5513/capnp-ts).
 */
import * as capnp from 'capnp-ts';
import * as capnp_ts_1 from 'capnp-ts';

export const _capnpFileId = BigInt('0xb4973e09eff2e05e');
export class KVIterable extends capnp_ts_1.Struct {
  /**
   * @param {capnp.Orphan<capnp.Pointer>} value
   */
  adoptKeys(value) {
    capnp_ts_1.Struct.adopt(value, capnp_ts_1.Struct.getPointer(0, this));
  }
  disownKeys() {
    return capnp_ts_1.Struct.disown(this.getKeys());
  }
  getKeys() {
    return capnp_ts_1.Struct.getList(0, capnp.DataList, this);
  }
  hasKeys() {
    return !capnp_ts_1.Struct.isNull(capnp_ts_1.Struct.getPointer(0, this));
  }
  /**
   * @param {number} length
   */
  initKeys(length) {
    return capnp_ts_1.Struct.initList(0, capnp.DataList, length, this);
  }
  /**
   * @param {capnp.Pointer} value
   */
  setKeys(value) {
    capnp_ts_1.Struct.copyFrom(value, capnp_ts_1.Struct.getPointer(0, this));
  }
  /**
   * @param {capnp.Orphan<capnp.Pointer>} value
   */
  adoptValues(value) {
    capnp_ts_1.Struct.adopt(value, capnp_ts_1.Struct.getPointer(1, this));
  }
  disownValues() {
    return capnp_ts_1.Struct.disown(this.getValues());
  }
  getValues() {
    return capnp_ts_1.Struct.getList(1, KVIterable._Values, this);
  }
  hasValues() {
    return !capnp_ts_1.Struct.isNull(capnp_ts_1.Struct.getPointer(1, this));
  }
  /**
   * @param {number} length
   */
  initValues(length) {
    return capnp_ts_1.Struct.initList(1, KVIterable._Values, length, this);
  }
  /**
   * @param {capnp.Pointer} value
   */
  setValues(value) {
    capnp_ts_1.Struct.copyFrom(value, capnp_ts_1.Struct.getPointer(1, this));
  }
  toString() {
    return 'KVIterable_' + super.toString();
  }
}
KVIterable._capnp = {
  displayName: 'KVIterable',
  id: 'edaa1b80ab4d437e',
  size: new capnp_ts_1.ObjectSize(0, 2)
};
KVIterable._Values = capnp.PointerList(capnp.DataList);
