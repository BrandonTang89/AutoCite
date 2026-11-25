(function ($) {
    var class2type = {};

    'Boolean Number String Function Array Date RegExp Object Error Symbol BigInt'.split(' ').forEach(function (name) {
        class2type['[object ' + name + ']'] = name.toLowerCase();
    });

    // Fomantic UI 2.9.4 still uses jQuery's removed type helper.
    $.type = function (value) {
        if (value == null) {
            return String(value);
        }

        var type = typeof value;
        return type === 'object' || type === 'function'
            ? class2type[Object.prototype.toString.call(value)] || 'object'
            : type;
    };
})(jQuery);
