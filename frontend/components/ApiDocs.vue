<template>
  <p class="text-xl text-right">Полную документацию можно найти <nuxt-link to="https://app.swaggerhub.com/apis/berzezek/FR-API/1.0.0" class="text-primary-400">здесь</nuxt-link></p>
  <h1>FR</h1>
  <div class="app-desc">Test service</div>
  <div class="app-desc">More information: <a href="https://helloreverb.com">https://helloreverb.com</a></div>
  <div class="app-desc">Contact Info: <a href="wknduz@gmail.com">wknduz@gmail.com</a></div>
  <div class="app-desc">Version: 1.0.0-oas3</div>

  <div class="license-info">All rights reserved</div>
  <div class="license-url">http://apache.org/licenses/LICENSE-2.0.html</div>
  <h2>Access</h2>
  <ol>
    <li>APIKey KeyParamName:Token KeyInQuery:false KeyInHeader:true</li>
    <li>HTTP Basic Authentication</li>
  </ol>

  <h2><a name="__Methods">Methods</a></h2>
  [ Jump to <a href="#__Models">Models</a> ]

  <h3>Table of Contents </h3>
  <div class="method-summary"></div>
  <h4><a href="#Customer">Customer</a></h4>
  <ul>
    <li><a href="#addCustomer"><code><span class="http-method">post</span> /api/v1/customer/</code></a></li>
    <li><a href="#deleteCustomer"><code><span class="http-method">delete</span> /api/v1/customer/{id}/</code></a></li>
    <li><a href="#getCustomers"><code><span class="http-method">get</span> /api/v1/customer/</code></a></li>
    <li><a href="#updateCustomer"><code><span class="http-method">put</span> /api/v1/customer/{id}/</code></a></li>
  </ul>
  <h4><a href="#Newsletter">Newsletter</a></h4>
  <ul>
    <li><a href="#addNewsletter"><code><span class="http-method">post</span> /api/v1/newsletter/</code></a></li>
    <li><a href="#deleteNewsletter"><code><span class="http-method">delete</span> /api/v1/newsletter/{id}/</code></a>
    </li>
    <li><a href="#getNewsletters"><code><span class="http-method">get</span> /api/v1/newsletter/</code></a></li>
    <li><a href="#updateNewsletter"><code><span class="http-method">put</span> /api/v1/newsletter/{id}/</code></a></li>
  </ul>
  <h4><a href="#NewsletterStatistic">NewsletterStatistic</a></h4>
  <ul>
    <li><a href="#addNewsletterStatistic"><code><span class="http-method">post</span>
      /api/v1/newsletter-statistic/</code></a></li>
    <li><a href="#getNewslettersStatistic"><code><span class="http-method">get</span>
      /api/v1/newsletter-statistic/</code></a></li>
  </ul>
  <h4><a href="#User">User</a></h4>
  <ul>
    <li><a href="#addUser"><code><span class="http-method">post</span> /auth/users/</code></a></li>
    <li><a href="#getToken"><code><span class="http-method">post</span> /auth/token/login/</code></a></li>
    <li><a href="#getUser"><code><span class="http-method">get</span> /auth/users/me/</code></a></li>
    <li><a href="#logoutUser"><code><span class="http-method">post</span> /auth/logout/</code></a></li>
  </ul>

  <h1><a name="Customer">Customer</a></h1>
  <div class="method"><a name="addCustomer"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="post"><code class="huge"><span class="http-method">post</span> /api/v1/customer/</code></pre>
    </div>
    <div class="method-summary">Add a new customer (<span class="nickname">addCustomer</span>)</div>
    <div class="method-notes"></div>


    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#Customer">Customer</a> (required)</div>

      <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; Pet object that needs to be added
        to the store
      </div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="deleteCustomer"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="delete"><code class="huge"><span class="http-method">delete</span> /api/v1/customer/{id}/</code></pre>
    </div>
    <div class="method-summary">Deletes a customer (<span class="nickname">deleteCustomer</span>)</div>
    <div class="method-notes"></div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">id (required)</div>

      <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash; Customer id to delete format: int64
      </div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">400</h4>
    Invalid ID supplied
    <a href="#"></a>
    <h4 class="field-label">404</h4>
    Customer not found
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="getCustomers"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="get"><code class="huge"><span class="http-method">get</span> /api/v1/customer/</code></pre>
    </div>
    <div class="method-summary">Get customers (<span class="nickname">getCustomers</span>)</div>
    <div class="method-notes">get customers list</div>


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      array[<a href="#Customer">Customer</a>]

    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>[ {
  "customer_time_zone" : "Europe/Moscow",
  "phone_number" : "12345678",
  "id" : 0,
  "tag" : "foo-tag",
  "phone_prefix" : "+7"
}, {
  "customer_time_zone" : "Europe/Moscow",
  "phone_number" : "12345678",
  "id" : 0,
  "tag" : "foo-tag",
  "phone_prefix" : "+7"
} ]</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    successful operation

    <h4 class="field-label">400</h4>
    Invalid status value
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="updateCustomer"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="put"><code class="huge"><span class="http-method">put</span> /api/v1/customer/{id}/</code></pre>
    </div>
    <div class="method-summary">Update an existing customer (<span class="nickname">updateCustomer</span>)</div>
    <div class="method-notes"></div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">id (required)</div>

      <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash; ID of customer to return format:
        int64
      </div>
    </div>  <!-- field-items -->

    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#Customer">Customer</a> (required)</div>

      <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; Customer object that needs to be
        added
      </div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">400</h4>
    Invalid ID supplied
    <a href="#"></a>
    <h4 class="field-label">404</h4>
    Customer not found
    <a href="#"></a>
    <h4 class="field-label">405</h4>
    Validation exception
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <h1><a name="Newsletter">Newsletter</a></h1>
  <div class="method"><a name="addNewsletter"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="post"><code class="huge"><span class="http-method">post</span> /api/v1/newsletter/</code></pre>
    </div>
    <div class="method-summary">Add a new newsletter (<span class="nickname">addNewsletter</span>)</div>
    <div class="method-notes"></div>


    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#Newsletter">Newsletter</a> (required)</div>

      <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; Pet object that needs to be added
        to the store
      </div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="deleteNewsletter"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="delete"><code class="huge"><span
          class="http-method">delete</span> /api/v1/newsletter/{id}/</code></pre>
    </div>
    <div class="method-summary">Deletes a newsletter (<span class="nickname">deleteNewsletter</span>)</div>
    <div class="method-notes"></div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">id (required)</div>

      <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash; Newsletter id to delete format:
        int64
      </div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">400</h4>
    Invalid ID supplied
    <a href="#"></a>
    <h4 class="field-label">404</h4>
    Newsletter not found
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="getNewsletters"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="get"><code class="huge"><span class="http-method">get</span> /api/v1/newsletter/</code></pre>
    </div>
    <div class="method-summary">Get newsletters (<span class="nickname">getNewsletters</span>)</div>
    <div class="method-notes">get newsletters list</div>


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      array[<a href="#Newsletter">Newsletter</a>]

    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>[ {
  "start_launch_date" : "2023-01-01",
  "customer_filter" : "foo-filter",
  "id" : 0,
  "end_launch_date" : "2023-01-02",
  "message" : "foo-message"
}, {
  "start_launch_date" : "2023-01-01",
  "customer_filter" : "foo-filter",
  "id" : 0,
  "end_launch_date" : "2023-01-02",
  "message" : "foo-message"
} ]</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    successful operation

    <h4 class="field-label">400</h4>
    Invalid status value
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="updateNewsletter"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="put"><code class="huge"><span class="http-method">put</span> /api/v1/newsletter/{id}/</code></pre>
    </div>
    <div class="method-summary">Update an existing newsletter (<span class="nickname">updateNewsletter</span>)</div>
    <div class="method-notes"></div>

    <h3 class="field-label">Path parameters</h3>
    <div class="field-items">
      <div class="param">id (required)</div>

      <div class="param-desc"><span class="param-type">Path Parameter</span> &mdash; ID of newsletter to return format:
        int64
      </div>
    </div>  <!-- field-items -->

    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#Newsletter">Newsletter</a> (required)</div>

      <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; Newsletter object that needs to be
        added
      </div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">400</h4>
    Invalid ID supplied
    <a href="#"></a>
    <h4 class="field-label">404</h4>
    Customer not found
    <a href="#"></a>
    <h4 class="field-label">405</h4>
    Validation exception
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <h1><a name="NewsletterStatistic">NewsletterStatistic</a></h1>
  <div class="method"><a name="addNewsletterStatistic"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="post"><code class="huge"><span
          class="http-method">post</span> /api/v1/newsletter-statistic/</code></pre>
    </div>
    <div class="method-summary">Add a new newsletter-statistic (<span class="nickname">addNewsletterStatistic</span>)
    </div>
    <div class="method-notes">Start Newsletter service</div>


    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#Newsletter-Statistic">Newsletter-Statistic</a> (required)</div>

      <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; Start Newsletter service</div>
    </div>  <!-- field-items -->


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="getNewslettersStatistic"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="get"><code class="huge"><span
          class="http-method">get</span> /api/v1/newsletter-statistic/</code></pre>
    </div>
    <div class="method-summary">Get newsletter-statistic (<span class="nickname">getNewslettersStatistic</span>)</div>
    <div class="method-notes">get newsletter-statistic list</div>


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      array[<a href="#Newsletter-Statistic">Newsletter-Statistic</a>]

    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>[ {
  "newsletter" : [ {
    "start_launch_date" : "2023-01-01",
    "customer_filter" : "foo-filter",
    "id" : 0,
    "end_launch_date" : "2023-01-02",
    "message" : "foo-message"
  }, {
    "start_launch_date" : "2023-01-01",
    "customer_filter" : "foo-filter",
    "id" : 0,
    "end_launch_date" : "2023-01-02",
    "message" : "foo-message"
  } ],
  "id" : 0,
  "customer" : [ {
    "customer_time_zone" : "Europe/Moscow",
    "phone_number" : "12345678",
    "id" : 0,
    "tag" : "foo-tag",
    "phone_prefix" : "+7"
  }, {
    "customer_time_zone" : "Europe/Moscow",
    "phone_number" : "12345678",
    "id" : 0,
    "tag" : "foo-tag",
    "phone_prefix" : "+7"
  } ]
}, {
  "newsletter" : [ {
    "start_launch_date" : "2023-01-01",
    "customer_filter" : "foo-filter",
    "id" : 0,
    "end_launch_date" : "2023-01-02",
    "message" : "foo-message"
  }, {
    "start_launch_date" : "2023-01-01",
    "customer_filter" : "foo-filter",
    "id" : 0,
    "end_launch_date" : "2023-01-02",
    "message" : "foo-message"
  } ],
  "id" : 0,
  "customer" : [ {
    "customer_time_zone" : "Europe/Moscow",
    "phone_number" : "12345678",
    "id" : 0,
    "tag" : "foo-tag",
    "phone_prefix" : "+7"
  }, {
    "customer_time_zone" : "Europe/Moscow",
    "phone_number" : "12345678",
    "id" : 0,
    "tag" : "foo-tag",
    "phone_prefix" : "+7"
  } ]
} ]</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    successful operation

    <h4 class="field-label">400</h4>
    Invalid status value
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <h1><a name="User">User</a></h1>
  <div class="method"><a name="addUser"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="post"><code class="huge"><span class="http-method">post</span> /auth/users/</code></pre>
    </div>
    <div class="method-summary">Add a new user (<span class="nickname">addUser</span>)</div>
    <div class="method-notes"></div>


    <h3 class="field-label">Consumes</h3>
    This API call consumes the following media types via the <span class="header">Content-Type</span> request header:
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Request body</h3>
    <div class="field-items">
      <div class="param">body <a href="#User">User</a> (required)</div>

      <div class="param-desc"><span class="param-type">Body Parameter</span> &mdash; add a new user</div>
    </div>  <!-- field-items -->


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#User">User</a>

    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
  "password" : "password",
  "id" : 0,
  "login" : "Foo"
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">201</h4>
    Created
    <a href="#User">User</a>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="getToken"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="post"><code class="huge"><span class="http-method">post</span> /auth/token/login/</code></pre>
    </div>
    <div class="method-summary">Get token (<span class="nickname">getToken</span>)</div>
    <div class="method-notes"></div>


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="getUser"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="get"><code class="huge"><span class="http-method">get</span> /auth/users/me/</code></pre>
    </div>
    <div class="method-summary">Add a new user (<span class="nickname">getUser</span>)</div>
    <div class="method-notes"></div>


    <h3 class="field-label">Return type</h3>
    <div class="return-type">
      <a href="#User">User</a>

    </div>

    <!--Todo: process Response Object and its headers, schema, examples -->

    <h3 class="field-label">Example data</h3>
    <div class="example-data-content-type">Content-Type: application/json</div>
    <pre class="example"><code>{
  "password" : "password",
  "id" : 0,
  "login" : "Foo"
}</code></pre>

    <h3 class="field-label">Produces</h3>
    This API call produces the following media types according to the <span class="header">Accept</span> request header;
    the media type will be conveyed by the <span class="header">Content-Type</span> response header.
    <ul>
      <li><code>application/json</code></li>
    </ul>

    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    get user object
    <a href="#User">User</a>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>
  <div class="method"><a name="logoutUser"></a>
    <div class="method-path">
      <a class="up" href="#__Methods">Up</a>
      <pre class="post"><code class="huge"><span class="http-method">post</span> /auth/logout/</code></pre>
    </div>
    <div class="method-summary">Logout user (<span class="nickname">logoutUser</span>)</div>
    <div class="method-notes"></div>


    <!--Todo: process Response Object and its headers, schema, examples -->


    <h3 class="field-label">Responses</h3>
    <h4 class="field-label">200</h4>
    Logout success
    <a href="#"></a>
    <h4 class="field-label">405</h4>
    Invalid input
    <a href="#"></a>
  </div> <!-- method -->
  <hr/>

  <h2><a name="__Models">Models</a></h2>
  [ Jump to <a href="#__Methods">Methods</a> ]

  <h3>Table of Contents</h3>
  <ol>
    <li><a href="#Customer"><code>Customer</code></a></li>
    <li><a href="#Newsletter"><code>Newsletter</code></a></li>
    <li><a href="#Newsletter-Statistic"><code>Newsletter-Statistic</code></a></li>
    <li><a href="#User"><code>User</code></a></li>
  </ol>

  <div class="model">
    <h3><a name="Customer"><code>Customer</code></a> <a class="up" href="#__Models">Up</a></h3>

    <div class="field-items">
      <div class="param">id (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#long">Long</a></span> format: int64</div>
      <div class="param">phone_number (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: 12345678</span></div>
      <div class="param">phone_prefix (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: +7</span></div>
      <div class="param">tag (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: foo-tag</span></div>
      <div class="param">customer_time_zone (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: Europe/Moscow</span></div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="Newsletter"><code>Newsletter</code></a> <a class="up" href="#__Models">Up</a></h3>

    <div class="field-items">
      <div class="param">id (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#long">Long</a></span> format: int64</div>
      <div class="param">start_launch_date (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: 2023-01-01</span></div>
      <div class="param">end_launch_date (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: 2023-01-02</span></div>
      <div class="param">customer_filter (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: foo-filter</span></div>
      <div class="param">message (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: foo-message</span></div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="Newsletter-Statistic"><code>Newsletter-Statistic</code></a> <a class="up" href="#__Models">Up</a></h3>

    <div class="field-items">
      <div class="param">id (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#long">Long</a></span> format: int64</div>
      <div class="param">newsletter (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#Newsletter">array[Newsletter]</a></span></div>
      <div class="param">customer (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#Customer">array[Customer]</a></span></div>
    </div>  <!-- field-items -->
  </div>
  <div class="model">
    <h3><a name="User"><code>User</code></a> <a class="up" href="#__Models">Up</a></h3>

    <div class="field-items">
      <div class="param">id (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#long">Long</a></span> format: int64</div>
      <div class="param">login (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span></div>
      <div class="param-desc"><span class="param-type">example: Foo</span></div>
      <div class="param">password (optional)</div>
      <div class="param-desc"><span class="param-type"><a href="#string">String</a></span> Must be longer than 8 letter
      </div>
    </div>  <!-- field-items -->
  </div>
</template>

<script>
export default {
  name: "ApiJson"
}
</script>

<style scoped>

body {
  font-family: Trebuchet MS, sans-serif;
  font-size: 15px;
  color: #444;
  /*margin-right: 24px;*/
}

h1 {
  font-size: 25px;
}

h2 {
  font-size: 20px;
}

h3 {
  font-size: 16px;
  font-weight: bold;
}

hr {
  height: 1px;
  border: 0;
  color: #ddd;
  background-color: #ddd;
}

.app-desc {
  clear: both;
  /*margin-left: 20px;*/
}

.param-name {
  width: 100%;
}

.license-info {
  /*margin-left: 20px;*/
}

.license-url {
  /*margin-left: 20px;*/
}

.model {
  margin: 0 0 0px 20px;
}

.method {
  /*margin-left: 20px;*/
}

.method-notes {
  margin: 10px 0 20px 0;
  font-size: 90%;
  color: #555;
}

pre {
  padding: 10px;
  margin-bottom: 2px;
}

.http-method {
  text-transform: uppercase;
}

pre.get {
  background-color: #0f6ab4;
}

pre.post {
  background-color: #10a54a;
}

pre.put {
  background-color: #c5862b;
}

pre.delete {
  background-color: #a41e22;
}

.huge {
  color: #fff;
}

pre.example {
  background-color: #f3f3f3;
  padding: 10px;
  border: 1px solid #ddd;
}

code {
  white-space: pre;
}

.nickname {
  font-weight: bold;
}

.method-path {
  font-size: 1.5em;
  background-color: #0f6ab4;
}

.up {
  float: right;
}

.parameter {
  width: 500px;
}

.param {
  width: 500px;
  padding: 10px 0 0 20px;
  font-weight: bold;
}

.param-desc {
  width: 700px;
  padding: 0 0 0 20px;
  color: #777;
}

.param-type {
  font-style: italic;
}

.param-enum-header {
  width: 700px;
  padding: 0 0 0 60px;
  color: #777;
  font-weight: bold;
}

.param-enum {
  width: 700px;
  padding: 0 0 0 80px;
  color: #777;
  font-style: italic;
}

.field-label {
  padding: 0;
  margin: 0;
  clear: both;
}

.field-items {
  padding: 0 0 15px 0;
  margin-bottom: 15px;
}

.return-type {
  clear: both;
  padding-bottom: 10px;
}

.param-header {
  font-weight: bold;
}

.method-tags {
  text-align: right;
}

.method-tag {
  background: none repeat scroll 0% 0% #24A600;
  border-radius: 3px;
  padding: 2px 10px;
  margin: 2px;
  color: #FFF;
  display: inline-block;
  text-decoration: none;
}
</style>