---
title: 代理(Proxy) 基本原理
---

## 代理(Proxy) 基本原理

### 创建一个贯通的代理(Proxy)

在代理对象上执行的所有操作都将透明地传播到目标对象。

```javascript
const target = {
  id: 'target'
}
const handler = {}
const proxy = new Proxy(target, handler)
// 'id'属性将得到相同的值
console.log(target.id) // target
console.log(proxy.id) // target
// Assignment to a target property changes both since
// both are accessing the same value.
target.id = 'foo'
console.log(target.id) // foo
console.log(proxy.id) // foo
// Assignment to a proxy property changes both since
// this assignment is conferred to the target object.
proxy.id = 'bar'
console.log(target.id) // bar
console.log(proxy.id) // bar
// The hasOwnProperty() method is effectively applied
// to the target in both cases.
console.log(target.hasOwnProperty('id')) // true
console.log(proxy.hasOwnProperty('id')) // true
```

### 定义陷阱（trap）

代理的主要目的是允许定义陷阱，基本操作在代理对象上被调用时，在目标对象上被调用之前，代理将调用trap函数，从而允许拦截和修改它的行为。

```js
const target = {
  foo: 'bar'
};
const handler = {
// Traps are keyed by method name inside the handler object
  get() {
    return 'handler override';
  }
};
const proxy = new Proxy(target, handler);
console.log(target.foo); // bar
console.log(proxy.foo); // handler override
console.log(target['foo']); // bar
console.log(proxy['foo']); // handler override
```

### 陷阱的参数和反射(Reflect) API

get 方法接收对目标对象的引用、正在查找的属性和代理对象的引用

```js
const target = {
  foo: 'bar'
}
const handler = {
  get(trapTarget, property, receiver) {
    console.log(trapTarget === target)
    console.log(property)
    console.log(receiver === proxy)
  }
}
const proxy = new Proxy(target, handler)
proxy.foo
// true
// foo
// true
```

### Proxying a Proxy

Proxy 可以拦截 Reflect API 的操作，这意味着完全可以创建一个代理（Proxy）的代理

```javascript
const target = {
  foo: 'bar'
}

const firstProxy = new Proxy(target, {
  get() {
    console.log('first proxy')
    return Reflect.get(...arguments)
  }
})

const secondProxy = new Proxy(firstProxy, {
  get() {
    console.log('second proxy')
    return Reflect.get(...arguments)
  }
})

console.log(secondProxy.foo)
// second proxy
// first proxy
// bar
```

## Proxy 陷阱 和 Reflect 方法

## Proxy 模式

## 总结
