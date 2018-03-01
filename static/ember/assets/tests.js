'use strict';

define('wistem-app-frontend/tests/app.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | app');

  QUnit.test('adapters/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'adapters/application.js should pass ESLint\n\n');
  });

  QUnit.test('app.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'app.js should pass ESLint\n\n');
  });

  QUnit.test('components/add-award.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/add-award.js should pass ESLint\n\n');
  });

  QUnit.test('components/award-display.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/award-display.js should pass ESLint\n\n');
  });

  QUnit.test('components/award-listing.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/award-listing.js should pass ESLint\n\n');
  });

  QUnit.test('components/edit-award.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/edit-award.js should pass ESLint\n\n');
  });

  QUnit.test('components/view-list-button.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'components/view-list-button.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/application.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/application.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/awards.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'controllers/awards.js should pass ESLint\n\n18:32 - \'$\' is not defined. (no-undef)');
  });

  QUnit.test('controllers/edit-award.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'controllers/edit-award.js should pass ESLint\n\n7:7 - Unexpected console statement. (no-console)\n11:7 - Unexpected console statement. (no-console)');
  });

  QUnit.test('controllers/login.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'controllers/login.js should pass ESLint\n\n');
  });

  QUnit.test('controllers/register.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'controllers/register.js should pass ESLint\n\n5:48 - \'department\' is defined but never used. (no-unused-vars)');
  });

  QUnit.test('controllers/search.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'controllers/search.js should pass ESLint\n\n8:32 - \'$\' is not defined. (no-undef)');
  });

  QUnit.test('initializers/auth-manager.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'initializers/auth-manager.js should pass ESLint\n\n');
  });

  QUnit.test('initializers/navigation.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'initializers/navigation.js should pass ESLint\n\n');
  });

  QUnit.test('initializers/notification-messages.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'initializers/notification-messages.js should pass ESLint\n\n');
  });

  QUnit.test('models/applicanttype.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/applicanttype.js should pass ESLint\n\n');
  });

  QUnit.test('models/areaofinterest.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/areaofinterest.js should pass ESLint\n\n');
  });

  QUnit.test('models/award.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/award.js should pass ESLint\n\n');
  });

  QUnit.test('models/awardpurpose.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/awardpurpose.js should pass ESLint\n\n');
  });

  QUnit.test('models/profile.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/profile.js should pass ESLint\n\n');
  });

  QUnit.test('models/stemfield.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/stemfield.js should pass ESLint\n\n');
  });

  QUnit.test('models/user.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'models/user.js should pass ESLint\n\n');
  });

  QUnit.test('resolver.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'resolver.js should pass ESLint\n\n');
  });

  QUnit.test('router.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'router.js should pass ESLint\n\n');
  });

  QUnit.test('routes/awardinfo.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/awardinfo.js should pass ESLint\n\n');
  });

  QUnit.test('routes/awards.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/awards.js should pass ESLint\n\n');
  });

  QUnit.test('routes/index.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/index.js should pass ESLint\n\n');
  });

  QUnit.test('routes/login.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/login.js should pass ESLint\n\n');
  });

  QUnit.test('routes/register.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'routes/register.js should pass ESLint\n\n');
  });

  QUnit.test('routes/search.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'routes/search.js should pass ESLint\n\n5:17 - \'Ember\' is not defined. (no-undef)\n128:17 - \'Ember\' is not defined. (no-undef)\n136:17 - \'Ember\' is not defined. (no-undef)\n143:17 - \'Ember\' is not defined. (no-undef)\n153:17 - \'Ember\' is not defined. (no-undef)');
  });

  QUnit.test('services/auth-manager.js', function (assert) {
    assert.expect(1);
    assert.ok(false, 'services/auth-manager.js should pass ESLint\n\n35:3 - Unexpected console statement. (no-console)\n52:5 - Unexpected console statement. (no-console)\n82:5 - Unexpected console statement. (no-console)\n92:3 - Unexpected console statement. (no-console)\n96:5 - Unexpected console statement. (no-console)\n136:5 - Unexpected console statement. (no-console)\n151:5 - Unexpected console statement. (no-console)');
  });

  QUnit.test('services/navigation.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'services/navigation.js should pass ESLint\n\n');
  });
});
define('wistem-app-frontend/tests/helpers/destroy-app', ['exports'], function (exports) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = destroyApp;
  var run = Ember.run;
  function destroyApp(application) {
    run(application, 'destroy');
  }
});
define('wistem-app-frontend/tests/helpers/ember-basic-dropdown', ['exports', 'ember-basic-dropdown/test-support/helpers', 'ember-native-dom-helpers'], function (exports, _helpers, _emberNativeDomHelpers) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.nativeClick = exports.fireKeydown = exports.tapTrigger = exports.clickTrigger = exports.nativeTap = undefined;
  Object.defineProperty(exports, 'nativeTap', {
    enumerable: true,
    get: function () {
      return _helpers.nativeTap;
    }
  });
  Object.defineProperty(exports, 'clickTrigger', {
    enumerable: true,
    get: function () {
      return _helpers.clickTrigger;
    }
  });
  Object.defineProperty(exports, 'tapTrigger', {
    enumerable: true,
    get: function () {
      return _helpers.tapTrigger;
    }
  });
  Object.defineProperty(exports, 'fireKeydown', {
    enumerable: true,
    get: function () {
      return _helpers.fireKeydown;
    }
  });
  exports.default = _helpers.default;
  var nativeClick = exports.nativeClick = _emberNativeDomHelpers.click;
});
define('wistem-app-frontend/tests/helpers/ember-power-select', ['exports', 'ember-power-select/test-support/helpers'], function (exports, _helpers) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.selectChoose = exports.touchTrigger = exports.nativeTouch = exports.clickTrigger = exports.typeInSearch = exports.triggerKeydown = exports.nativeMouseUp = exports.nativeMouseDown = exports.findContains = undefined;
  exports.default = deprecatedRegisterHelpers;


  function deprecateHelper(fn, name) {
    return function () {
      (true && !(false) && Ember.deprecate('DEPRECATED `import { ' + name + ' } from \'../../tests/helpers/ember-power-select\';` is deprecated. Please, replace it with `import { ' + name + ' } from \'ember-power-select/test-support/helpers\';`', false, { until: '1.11.0', id: 'ember-power-select-test-support-' + name }));

      return fn.apply(undefined, arguments);
    };
  }

  var findContains = deprecateHelper(_helpers.findContains, 'findContains');
  var nativeMouseDown = deprecateHelper(_helpers.nativeMouseDown, 'nativeMouseDown');
  var nativeMouseUp = deprecateHelper(_helpers.nativeMouseUp, 'nativeMouseUp');
  var triggerKeydown = deprecateHelper(_helpers.triggerKeydown, 'triggerKeydown');
  var typeInSearch = deprecateHelper(_helpers.typeInSearch, 'typeInSearch');
  var clickTrigger = deprecateHelper(_helpers.clickTrigger, 'clickTrigger');
  var nativeTouch = deprecateHelper(_helpers.nativeTouch, 'nativeTouch');
  var touchTrigger = deprecateHelper(_helpers.touchTrigger, 'touchTrigger');
  var selectChoose = deprecateHelper(_helpers.selectChoose, 'selectChoose');

  function deprecatedRegisterHelpers() {
    (true && !(false) && Ember.deprecate("DEPRECATED `import registerPowerSelectHelpers from '../../tests/helpers/ember-power-select';` is deprecated. Please, replace it with `import registerPowerSelectHelpers from 'ember-power-select/test-support/helpers';`", false, { until: '1.11.0', id: 'ember-power-select-test-support-register-helpers' }));

    return (0, _helpers.default)();
  }

  exports.findContains = findContains;
  exports.nativeMouseDown = nativeMouseDown;
  exports.nativeMouseUp = nativeMouseUp;
  exports.triggerKeydown = triggerKeydown;
  exports.typeInSearch = typeInSearch;
  exports.clickTrigger = clickTrigger;
  exports.nativeTouch = nativeTouch;
  exports.touchTrigger = touchTrigger;
  exports.selectChoose = selectChoose;
});
define('wistem-app-frontend/tests/helpers/module-for-acceptance', ['exports', 'qunit', 'wistem-app-frontend/tests/helpers/start-app', 'wistem-app-frontend/tests/helpers/destroy-app'], function (exports, _qunit, _startApp, _destroyApp) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });

  exports.default = function (name) {
    var options = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : {};

    (0, _qunit.module)(name, {
      beforeEach: function beforeEach() {
        this.application = (0, _startApp.default)();

        if (options.beforeEach) {
          return options.beforeEach.apply(this, arguments);
        }
      },
      afterEach: function afterEach() {
        var _this = this;

        var afterEach = options.afterEach && options.afterEach.apply(this, arguments);
        return resolve(afterEach).then(function () {
          return (0, _destroyApp.default)(_this.application);
        });
      }
    });
  };

  var resolve = Ember.RSVP.resolve;
});
define('wistem-app-frontend/tests/helpers/resolver', ['exports', 'wistem-app-frontend/resolver', 'wistem-app-frontend/config/environment'], function (exports, _resolver, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });


  var resolver = _resolver.default.create();

  resolver.namespace = {
    modulePrefix: _environment.default.modulePrefix,
    podModulePrefix: _environment.default.podModulePrefix
  };

  exports.default = resolver;
});
define('wistem-app-frontend/tests/helpers/start-app', ['exports', 'wistem-app-frontend/app', 'wistem-app-frontend/config/environment'], function (exports, _app, _environment) {
  'use strict';

  Object.defineProperty(exports, "__esModule", {
    value: true
  });
  exports.default = startApp;
  var merge = Ember.merge;
  var run = Ember.run;
  function startApp(attrs) {
    var attributes = merge({}, _environment.default.APP);
    attributes = merge(attributes, attrs); // use defaults, but you can override;

    return run(function () {
      var application = _app.default.create(attributes);
      application.setupForTesting();
      application.injectTestHelpers();
      return application;
    });
  }
});
define('wistem-app-frontend/tests/integration/components/award-display-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('award-display', 'Integration | Component | award display', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "eIJc3h3h",
      "block": "{\"symbols\":[],\"statements\":[[1,[18,\"award-display\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "mfqkr+el",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"award-display\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('wistem-app-frontend/tests/integration/components/award-listing-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForComponent)('award-listing', 'Integration | Component | award listing', {
    integration: true
  });

  (0, _emberQunit.test)('it renders', function (assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.on('myAction', function(val) { ... });

    this.render(Ember.HTMLBars.template({
      "id": "erEfdEWS",
      "block": "{\"symbols\":[],\"statements\":[[1,[18,\"award-listing\"],false]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), '');

    // Template block usage:
    this.render(Ember.HTMLBars.template({
      "id": "fXBfsFRQ",
      "block": "{\"symbols\":[],\"statements\":[[0,\"\\n\"],[4,\"award-listing\",null,null,{\"statements\":[[0,\"      template block text\\n\"]],\"parameters\":[]},null],[0,\"  \"]],\"hasEval\":false}",
      "meta": {}
    }));

    assert.equal(this.$().text().trim(), 'template block text');
  });
});
define('wistem-app-frontend/tests/test-helper', ['wistem-app-frontend/tests/helpers/resolver', 'ember-qunit', 'ember-cli-qunit'], function (_resolver, _emberQunit, _emberCliQunit) {
  'use strict';

  (0, _emberQunit.setResolver)(_resolver.default);
  (0, _emberCliQunit.start)();
});
define('wistem-app-frontend/tests/tests.lint-test', [], function () {
  'use strict';

  QUnit.module('ESLint | tests');

  QUnit.test('helpers/destroy-app.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/destroy-app.js should pass ESLint\n\n');
  });

  QUnit.test('helpers/module-for-acceptance.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/module-for-acceptance.js should pass ESLint\n\n');
  });

  QUnit.test('helpers/resolver.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/resolver.js should pass ESLint\n\n');
  });

  QUnit.test('helpers/start-app.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'helpers/start-app.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/award-display-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/award-display-test.js should pass ESLint\n\n');
  });

  QUnit.test('integration/components/award-listing-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'integration/components/award-listing-test.js should pass ESLint\n\n');
  });

  QUnit.test('test-helper.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'test-helper.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/application-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/application-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/awards-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/awards-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/register-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/register-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/controllers/search-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/controllers/search-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/initializers/auth-manager-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/initializers/auth-manager-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/initializers/navigation-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/initializers/navigation-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/initializers/notification-messages-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/initializers/notification-messages-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/applicanttype-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/applicanttype-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/areaofinterest-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/areaofinterest-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/awardpurpose-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/awardpurpose-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/profile-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/profile-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/stemfield-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/stemfield-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/models/user-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/models/user-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/awardinfo-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/awardinfo-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/index-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/index-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/login-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/login-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/register-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/register-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/routes/search-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/routes/search-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/auth-manager-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/auth-manager-test.js should pass ESLint\n\n');
  });

  QUnit.test('unit/services/navigation-test.js', function (assert) {
    assert.expect(1);
    assert.ok(true, 'unit/services/navigation-test.js should pass ESLint\n\n');
  });
});
define('wistem-app-frontend/tests/unit/controllers/application-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('controller:application', 'Unit | Controller | application', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wistem-app-frontend/tests/unit/controllers/awards-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('controller:awards', 'Unit | Controller | awards', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wistem-app-frontend/tests/unit/controllers/register-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('controller:register', 'Unit | Controller | register', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wistem-app-frontend/tests/unit/controllers/search-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('controller:search', 'Unit | Controller | search', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var controller = this.subject();
    assert.ok(controller);
  });
});
define('wistem-app-frontend/tests/unit/initializers/auth-manager-test', ['wistem-app-frontend/initializers/auth-manager', 'qunit', 'wistem-app-frontend/tests/helpers/destroy-app'], function (_authManager, _qunit, _destroyApp) {
  'use strict';

  var Application = Ember.Application;
  var run = Ember.run;


  (0, _qunit.module)('Unit | Initializer | auth manager', {
    beforeEach: function beforeEach() {
      var _this = this;

      run(function () {
        _this.application = Application.create();
        _this.application.deferReadiness();
      });
    },
    afterEach: function afterEach() {
      (0, _destroyApp.default)(this.application);
    }
  });

  // Replace this with your real tests.
  (0, _qunit.test)('it works', function (assert) {
    (0, _authManager.initialize)(this.application);

    // you would normally confirm the results of the initializer here
    assert.ok(true);
  });
});
define('wistem-app-frontend/tests/unit/initializers/navigation-test', ['wistem-app-frontend/initializers/navigation', 'qunit', 'wistem-app-frontend/tests/helpers/destroy-app'], function (_navigation, _qunit, _destroyApp) {
  'use strict';

  var Application = Ember.Application;
  var run = Ember.run;


  (0, _qunit.module)('Unit | Initializer | navigation', {
    beforeEach: function beforeEach() {
      var _this = this;

      run(function () {
        _this.application = Application.create();
        _this.application.deferReadiness();
      });
    },
    afterEach: function afterEach() {
      (0, _destroyApp.default)(this.application);
    }
  });

  // Replace this with your real tests.
  (0, _qunit.test)('it works', function (assert) {
    (0, _navigation.initialize)(this.application);

    // you would normally confirm the results of the initializer here
    assert.ok(true);
  });
});
define('wistem-app-frontend/tests/unit/initializers/notification-messages-test', ['wistem-app-frontend/initializers/notification-messages', 'qunit', 'wistem-app-frontend/tests/helpers/destroy-app'], function (_notificationMessages, _qunit, _destroyApp) {
  'use strict';

  var Application = Ember.Application;
  var run = Ember.run;


  (0, _qunit.module)('Unit | Initializer | notification messages', {
    beforeEach: function beforeEach() {
      var _this = this;

      run(function () {
        _this.application = Application.create();
        _this.application.deferReadiness();
      });
    },
    afterEach: function afterEach() {
      (0, _destroyApp.default)(this.application);
    }
  });

  // Replace this with your real tests.
  (0, _qunit.test)('it works', function (assert) {
    (0, _notificationMessages.initialize)(this.application);

    // you would normally confirm the results of the initializer here
    assert.ok(true);
  });
});
define('wistem-app-frontend/tests/unit/models/applicanttype-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('applicanttype', 'Unit | Model | applicanttype', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('wistem-app-frontend/tests/unit/models/areaofinterest-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('areaofinterest', 'Unit | Model | areaofinterest', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('wistem-app-frontend/tests/unit/models/awardpurpose-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('awardpurpose', 'Unit | Model | awardpurpose', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('wistem-app-frontend/tests/unit/models/profile-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('profile', 'Unit | Model | profile', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('wistem-app-frontend/tests/unit/models/stemfield-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('stemfield', 'Unit | Model | stemfield', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('wistem-app-frontend/tests/unit/models/user-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleForModel)('user', 'Unit | Model | user', {
    // Specify the other units that are required for this test.
    needs: []
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var model = this.subject();
    // let store = this.store();
    assert.ok(!!model);
  });
});
define('wistem-app-frontend/tests/unit/routes/awardinfo-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('route:awardinfo', 'Unit | Route | awardinfo', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wistem-app-frontend/tests/unit/routes/index-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('route:index', 'Unit | Route | index', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wistem-app-frontend/tests/unit/routes/login-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('route:login', 'Unit | Route | login', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wistem-app-frontend/tests/unit/routes/register-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('route:register', 'Unit | Route | register', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wistem-app-frontend/tests/unit/routes/search-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('route:search', 'Unit | Route | search', {
    // Specify the other units that are required for this test.
    // needs: ['controller:foo']
  });

  (0, _emberQunit.test)('it exists', function (assert) {
    var route = this.subject();
    assert.ok(route);
  });
});
define('wistem-app-frontend/tests/unit/services/auth-manager-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('service:auth-manager', 'Unit | Service | auth manager', {
    // Specify the other units that are required for this test.
    // needs: ['service:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var service = this.subject();
    assert.ok(service);
  });
});
define('wistem-app-frontend/tests/unit/services/navigation-test', ['ember-qunit'], function (_emberQunit) {
  'use strict';

  (0, _emberQunit.moduleFor)('service:navigation', 'Unit | Service | navigation', {
    // Specify the other units that are required for this test.
    // needs: ['service:foo']
  });

  // Replace this with your real tests.
  (0, _emberQunit.test)('it exists', function (assert) {
    var service = this.subject();
    assert.ok(service);
  });
});
require('wistem-app-frontend/tests/test-helper');
EmberENV.TESTS_FILE_LOADED = true;
//# sourceMappingURL=tests.map
