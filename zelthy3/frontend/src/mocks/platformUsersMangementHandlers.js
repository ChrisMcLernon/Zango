import { rest } from 'msw';
import moment from 'moment';
import { faker } from '@faker-js/faker';

const range = (len) => {
	const arr = [];
	for (let i = 0; i < len; i++) {
		arr.push(i);
	}
	return arr;
};

const newApp = () => {
	return {
		id: faker.number.int(1000),
		schema_name: faker.internet.displayName(),
		created_at: faker.date.past(),
		created_by: faker.person.fullName(),
		modified_at: faker.date.past(),
		modified_by: faker.person.fullName(),
		uuid: faker.number.int({ min: 1000, max: 9999 }),
		name: 'App ' + faker.number.int({ min: 1, max: 10 }),
		description: faker.lorem.sentences(2),
		tenant_type: 'app',
		status: faker.helpers.shuffle(['staged', 'deployed']),
		deployed_on: null,
		suspended_on: null,
		deleted_on: null,
		timezone: null,
		language: null,
		date_format: null,
		datetime_format: null,
		logo: null,
		extra_config: null,
	};
};

const newUser = () => {
	return {
		id: faker.number.int({ min: 1000, max: 9999 }),
		name: faker.person.fullName(),
		email: faker.internet.email().toLowerCase(),
		apps: makeApps(faker.number.int({ min: 1, max: 10 })),
		is_superadmin: false,
		last_login: faker.date.past(),
		status: faker.helpers.shuffle(['active', 'inactive'])[0],
		created_at: faker.date.past(),
	};
};

export function makeApps(...lens) {
	const makeDataLevel = (depth = 0) => {
		const len = lens[depth];
		return range(len).map((d) => {
			return {
				...newApp(),
				subRows: lens[depth + 1] ? makeDataLevel(depth + 1) : undefined,
			};
		});
	};

	return makeDataLevel();
}

export function makeData(...lens) {
	const makeDataLevel = (depth = 0) => {
		const len = lens[depth];
		return range(len).map((d) => {
			return {
				...newUser(),
				subRows: lens[depth + 1] ? makeDataLevel(depth + 1) : undefined,
			};
		});
	};

	return makeDataLevel();
}

let totalData = 1000;
const data = makeData(totalData);

const platformUsersMockData = {
	total_records: 11,
	total_pages: 2,
	next: 'http://localhost:8000/api/v1/auth/platform-users/?page=2',
	previous: null,
	records: data,
};

export const platformUsersMangementHandlers = [
	rest.get('/api/v1/auth/platform-users/', (req, res, ctx) => {
		const pageIndex = parseInt(req.url.searchParams.get('pageIndex')) || 0;
		const pageSize = parseInt(req.url.searchParams.get('pageSize')) || 10;
		let slicedData = data.slice(
			pageIndex * pageSize,
			(pageIndex + 1) * pageSize
		);

		console.log(
			'slicedData',
			typeof pageIndex,
			typeof pageSize,
			pageIndex,
			pageSize,
			slicedData
		);
		return res(
			ctx.delay(500),
			ctx.status(200),
			ctx.json({
				success: true,
				response: {
					platform_users: {
						total_records: totalData,
						total_pages: Math.ceil(data.length / pageSize),
						next: 'http://localhost:8000/api/v1/auth/platform-users/?page=2',
						previous: null,
						records: slicedData,
					},
					include_dropdown_options: {
						apps: [],
					},
					message: 'Platform user fetched successfully',
				},
			})
		);
	}),
];
